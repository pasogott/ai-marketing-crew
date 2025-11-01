import os
from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools import (
    SerperDevTool,
    ScrapeWebsiteTool,
    DirectoryReadTool,
    FileReadTool,
    FileWriteTool,
)
from typing import List

# Erstelle resources/ Verzeichnis falls nicht vorhanden
resources_dir = Path("resources")
drafts_dir = resources_dir / "drafts"
resources_dir.mkdir(exist_ok=True)
drafts_dir.mkdir(exist_ok=True)


@CrewBase
class AiMarketingCrew():
    """AiMarketingCrew - Multi-Agent Marketing System basierend auf CrewAI"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Tools initialisieren (mit Fallback bei fehlenden API Keys)
    def _init_tools(self):
        """Initialisiere Tools mit Fehlerbehandlung"""
        tools = {}
        
        # SerperDevTool (Web Search)
        try:
            if os.getenv("SERPER_API_KEY"):
                tools["serper_dev_tool"] = SerperDevTool()
            else:
                print("WARNUNG: SERPER_API_KEY nicht gefunden. Web-Suche wird nicht verfügbar sein.")
        except Exception as e:
            print(f"WARNUNG: SerperDevTool konnte nicht initialisiert werden: {e}")

        # ScrapeWebsiteTool
        try:
            tools["scrape_website_tool"] = ScrapeWebsiteTool()
        except Exception as e:
            print(f"WARNUNG: ScrapeWebsiteTool konnte nicht initialisiert werden: {e}")

        # File/Directory Tools
        try:
            tools["directory_read_tool"] = DirectoryReadTool(directory="resources")
            tools["file_read_tool"] = FileReadTool()
            tools["file_write_tool"] = FileWriteTool()
        except Exception as e:
            print(f"WARNUNG: File/Directory Tools konnten nicht initialisiert werden: {e}")

        return tools

    def __init__(self):
        """Initialisiere Crew und Tools"""
        super().__init__()
        self.tools = self._init_tools()

    @agent
    def head_of_marketing(self) -> Agent:
        """Head of Marketing Agent"""
        agent_config = self.agents_config['head_of_marketing']
        # Tools für diesen Agent
        agent_tools = []
        for tool_name in agent_config.get('tools', []):
            if tool_name in self.tools:
                agent_tools.append(self.tools[tool_name])
        
        return Agent(
            config=agent_config,
            tools=agent_tools if agent_tools else None,
            verbose=True,
            allow_delegation=agent_config.get('allow_delegation', True),
            max_iter=agent_config.get('max_iter', 5),
        )

    @agent
    def content_creator_social(self) -> Agent:
        """Social Media Content Creator Agent"""
        agent_config = self.agents_config['content_creator_social']
        agent_tools = []
        for tool_name in agent_config.get('tools', []):
            if tool_name in self.tools:
                agent_tools.append(self.tools[tool_name])
        
        return Agent(
            config=agent_config,
            tools=agent_tools if agent_tools else None,
            verbose=True,
            max_iter=agent_config.get('max_iter', 3),
        )

    @agent
    def content_writer_blog(self) -> Agent:
        """Blog Content Writer Agent"""
        agent_config = self.agents_config['content_writer_blog']
        agent_tools = []
        for tool_name in agent_config.get('tools', []):
            if tool_name in self.tools:
                agent_tools.append(self.tools[tool_name])
        
        return Agent(
            config=agent_config,
            tools=agent_tools if agent_tools else None,
            verbose=True,
            max_iter=agent_config.get('max_iter', 3),
        )

    @agent
    def seo_specialist(self) -> Agent:
        """SEO Specialist Agent"""
        agent_config = self.agents_config['seo_specialist']
        agent_tools = []
        for tool_name in agent_config.get('tools', []):
            if tool_name in self.tools:
                agent_tools.append(self.tools[tool_name])
        
        return Agent(
            config=agent_config,
            tools=agent_tools if agent_tools else None,
            verbose=True,
            max_iter=agent_config.get('max_iter', 3),
        )

    @task
    def market_research_task(self) -> Task:
        """Marktforschungs-Task"""
        task_config = self.tasks_config['market_research_task']
        return Task(
            config=task_config,
            agent=self.head_of_marketing(),
            output_file=task_config.get('output_file', 'resources/market_research.md'),
        )

    @task
    def build_marketing_strategy_task(self) -> Task:
        """Marketing-Strategie Task"""
        task_config = self.tasks_config['build_marketing_strategy_task']
        return Task(
            config=task_config,
            agent=self.head_of_marketing(),
            context=[self.market_research_task()],
            output_file=task_config.get('output_file', 'resources/marketing_strategy.md'),
        )

    @task
    def build_content_calendar_task(self) -> Task:
        """Content-Kalender Task"""
        task_config = self.tasks_config['build_content_calendar_task']
        return Task(
            config=task_config,
            agent=self.content_creator_social(),
            context=[self.build_marketing_strategy_task()],
            output_file=task_config.get('output_file', 'resources/drafts/content_calendar.md'),
        )

    @task
    def generate_social_posts_task(self) -> Task:
        """Social Media Posts Task"""
        task_config = self.tasks_config['generate_social_posts_task']
        return Task(
            config=task_config,
            agent=self.content_creator_social(),
            context=[self.build_content_calendar_task()],
            output_file=task_config.get('output_file', 'resources/drafts/social_posts/'),
        )

    @task
    def generate_blog_draft_task(self) -> Task:
        """Blog-Entwurf Task"""
        task_config = self.tasks_config['generate_blog_draft_task']
        return Task(
            config=task_config,
            agent=self.content_writer_blog(),
            context=[
                self.market_research_task(),
                self.build_marketing_strategy_task(),
            ],
            output_file=task_config.get('output_file', 'resources/drafts/blog_post_autosheetiq.md'),
        )

    @task
    def generate_seo_keywords_task(self) -> Task:
        """SEO Keywords Task"""
        task_config = self.tasks_config['generate_seo_keywords_task']
        return Task(
            config=task_config,
            agent=self.seo_specialist(),
            context=[self.market_research_task()],
            output_file=task_config.get('output_file', 'resources/keywords.txt'),
        )

    @crew
    def crew(self) -> Crew:
        """Erstellt die AiMarketingCrew"""
        return Crew(
            agents=[
                self.head_of_marketing(),
                self.content_creator_social(),
                self.content_writer_blog(),
                self.seo_specialist(),
            ],
            tasks=[
                self.market_research_task(),
                self.build_marketing_strategy_task(),
                self.build_content_calendar_task(),
                self.generate_social_posts_task(),
                self.generate_blog_draft_task(),
                self.generate_seo_keywords_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )
