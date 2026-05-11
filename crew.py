from crewai import Agent, Crew, Process, Task
from langchain_community.llms import Ollama

# Utilisation explicite d'Ollama (local)
llm = Ollama(model="qwen3:14b", temperature=0.7)

# === Agents du LinkSphere Dev Crew ===
orchestrator = Agent(
    role="Orchestrator & Chef de Projet",
    goal="Diriger le développement de LinkSphere pour en faire l'assistant IA local le plus utile et grand public possible",
    backstory="Chef de projet ambitieux et organisé.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

architect = Agent(
    role="Architecte (Quantum Memory + Liquid Transformer + Dream Mode)",
    goal="Concevoir l'architecture complète de LinkSphere",
    backstory="Expert en systèmes de mémoire persistante et auto-évolutifs.",
    llm=llm
)

mobile_builder = Agent(
    role="Mobile & Desktop Builder",
    goal="Créer une app mobile-first (Android + iOS) + Desktop simple et belle",
    backstory="Spécialiste MLC LLM, Tauri et interfaces grand public.",
    llm=llm
)

dream_trainer = Agent(
    role="Dream Mode & Liquid Transformer Engineer",
    goal="Implémenter le Dream Mode et l'adaptation continue",
    backstory="Expert en Unsloth et fine-tuning incrémental.",
    llm=llm
)

distributor = Agent(
    role="Distributor & Growth",
    goal="Préparer les releases 1-clic et la stratégie d'adoption massive",
    backstory="Tu veux que LinkSphere soit utilisé quotidiennement par des centaines de milliers de personnes.",
    llm=llm
)

# === Tâches de démarrage ===
task1 = Task(
    description="Créer le Modelfile complet de LinkSphere avec personnalité, Quantum Memory, Liquid Transformer, Dream Mode et instructions mobile.",
    agent=architect,
    expected_output="Fichier Modelfile prêt à l'emploi."
)

task2 = Task(
    description="Créer la structure complète du projet (mobile, desktop, memory, dream_mode, scripts d'installation).",
    agent=mobile_builder,
    expected_output="Arborescence détaillée + fichiers de configuration initiaux."
)

task3 = Task(
    description="Écrire le script complet du Dream Mode (déclenchement nocturne, LoRA, gestion batterie).",
    agent=dream_trainer,
    expected_output="Script Python fonctionnel du Dream Mode."
)

crew = Crew(
    agents=[orchestrator, architect, mobile_builder, dream_trainer, distributor],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    memory=False,          # Désactivé pour éviter les problèmes d'embedder
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Lancement du LinkSphere Dev Crew...")
    result = crew.kickoff()
    print("\n=== LinkSphere Dev Crew a terminé sa première mission ===\n")
    print(result)

Fix crew.py - force local Ollama
