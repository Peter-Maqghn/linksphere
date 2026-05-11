from crewai import Agent, Crew, Process, Task
from langchain_ollama import ChatOllama

# Modèle local Ollama
llm = ChatOllama(model="qwen3:14b", temperature=0.7)

# Agents simplifiés
orchestrator = Agent(
    role="Orchestrator",
    goal="Coordonner le développement de LinkSphere",
    backstory="Chef de projet efficace.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

architect = Agent(
    role="Architecte",
    goal="Créer le Modelfile complet de LinkSphere",
    backstory="Expert en IA locale.",
    verbose=True,
    llm=llm
)

mobile_builder = Agent(
    role="Mobile Builder",
    goal="Créer la structure du projet mobile et desktop",
    backstory="Spécialiste applications locales.",
    verbose=True,
    llm=llm
)

crew = Crew(
    agents=[orchestrator, architect, mobile_builder],
    tasks=[
        Task(
            description="Créer le Modelfile complet de LinkSphere avec personnalité, Quantum Memory, Liquid Transformer, Dream Mode et instructions mobile.",
            agent=architect,
            expected_output="Fichier Modelfile prêt à l'emploi."
        ),
        Task(
            description="Créer la structure complète du projet (dossiers mobile, desktop, memory, dream_mode, etc.).",
            agent=mobile_builder,
            expected_output="Arborescence détaillée du projet."
        )
    ],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Lancement du LinkSphere Dev Crew (version simplifiée)...")
    result = crew.kickoff()
    print("\n=== LinkSphere Dev Crew a terminé ===\n")
    print(result)

Fix crew.py - version Ollama simplifiée
