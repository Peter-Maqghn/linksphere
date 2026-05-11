from crewai import Agent, Crew, Process, Task
from langchain_ollama import ChatOllama

# Modèle local Ollama
llm = ChatOllama(model="qwen3:14b", temperature=0.7)

# Agents
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

# Tâches
task1 = Task(
    description="Créer le Modelfile complet de LinkSphere avec personnalité, Quantum Memory, Liquid Transformer, Dream Mode et instructions mobile.",
    agent=architect,
    expected_output="Fichier Modelfile prêt à l'emploi."
)

task2 = Task(
    description="Créer la structure complète du projet (mobile, desktop, memory, dream_mode, etc.).",
    agent=mobile_builder,
    expected_output="Arborescence détaillée du projet."
)

crew = Crew(
    agents=[orchestrator, architect, mobile_builder],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Lancement du LinkSphere Dev Crew...")
    result = crew.kickoff()
    print("\n=== LinkSphere Dev Crew a terminé ===\n")
    print(result)

Crew.py - version propre finale
