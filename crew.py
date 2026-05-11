cat > linksphere/crew/crew.py << 'EOF'
from crewai import Agent, Crew, Process, Task

# === Agents du LinkSphere Dev Crew ===
orchestrator = Agent(
    role="Orchestrator & Chef de Projet",
    goal="Diriger le développement de LinkSphere pour en faire l'assistant IA local le plus utile et grand public possible",
    backstory="Chef de projet ambitieux et organisé.",
    verbose=True,
    allow_delegation=True,
    llm="ollama/qwen3:14b"
)

architect = Agent(
    role="Architecte (Quantum Memory + Liquid Transformer + Dream Mode)",
    goal="Concevoir l'architecture complète de LinkSphere",
    backstory="Expert en systèmes de mémoire persistante et auto-évolutifs.",
    llm="ollama/qwen3:14b"
)

mobile_builder = Agent(
    role="Mobile & Desktop Builder",
    goal="Créer une app mobile-first (Android + iOS) + Desktop simple et belle",
    backstory="Spécialiste MLC LLM, Tauri et interfaces grand public.",
    llm="ollama/llama3.2:8b"
)

dream_trainer = Agent(
    role="Dream Mode & Liquid Transformer Engineer",
    goal="Implémenter le Dream Mode et l'adaptation continue",
    backstory="Expert en Unsloth et fine-tuning incrémental.",
    llm="ollama/qwen3:14b"
)

distributor = Agent(
    role="Distributor & Growth",
    goal="Préparer les releases 1-clic et la stratégie d'adoption massive",
    backstory="Tu veux que LinkSphere soit utilisé quotidiennement par des centaines de milliers de personnes.",
    llm="ollama/llama3.2:8b"
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
    memory=True,
    verbose=2
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== LinkSphere Dev Crew a terminé sa première mission ===\n")
    print(result)
EOF

Fix crew.py syntax
