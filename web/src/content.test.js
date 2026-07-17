import { describe, expect, it } from "vitest";
import { catalog, parseReadmeUseCases, slugify, stripMarkdown } from "./content.js";

describe("catalog content", () => {
  it("normalizes display text and slugs", () => {
    expect(stripMarkdown("**PDF [Q&A](https://example.com)**")).toBe("PDF Q&A");
    expect(slugify("CrewAI + MCP Tools")).toBe("crewai-mcp-tools");
  });

  it("parses use-case tables with source context", () => {
    const markdown = `
## CrewAI

| Use Case | Industry | Description | GitHub |
|---|---|---|---|
| Research Crew | Research | Finds and summarizes sources | [Code](https://example.com/research) |
`;
    expect(parseReadmeUseCases(markdown)).toEqual([
      expect.objectContaining({
        title: "Research Crew",
        industry: "Research",
        framework: "CrewAI",
        url: "https://example.com/research",
      }),
    ]);
  });

  it("builds the complete local catalog from repository files", () => {
    expect(catalog.agents).toHaveLength(20);
    expect(catalog.courseLessons).toHaveLength(3);
    expect(catalog.useCases.length).toBeGreaterThanOrEqual(100);
    expect(catalog.useCases.filter((item) => item.linkStatus === "unavailable")).toHaveLength(35);
  });
});
