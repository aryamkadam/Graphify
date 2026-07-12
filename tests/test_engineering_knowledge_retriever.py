from pprint import pprint

from graph_builder.knowledge.engineering_knowledge_retriever import (
    EngineeringKnowledgeRetriever,
)

from graph_builder.workers.engineering_review_cycle import (
    EngineeringReviewCycle,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Knowledge Retriever")
print("========================================\n")

retriever = EngineeringKnowledgeRetriever()

cycle = EngineeringReviewCycle()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

    priority="HIGH",

)

task.start()

review = cycle.execute(task)

print("Remember\n")

pprint(

    retriever.remember(review)

)

print("\nKnowledge Summary\n")

pprint(

    retriever.knowledge_summary()

)

print("\nRetrieve by Title\n")

pprint(

    retriever.retrieve_by_title(

        "Implement Runtime Scheduler",

    )

)

print("\nLatest Experience\n")

pprint(

    retriever.latest_experience()

)