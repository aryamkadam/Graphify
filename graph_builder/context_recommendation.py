def generate_context_recommendations(
    context
):

    repository = context["repository"]

    recommendations = []

    for item in repository[
        "top_recommendations"
    ]:

        recommendations.append({

            "priority":
                item["priority"],

            "message":
                item["message"],

            "score":
                item["score"]
        })

    return {

        "health_score":
            repository[
                "health_score"
            ],

        "recommendation_count":
            len(
                recommendations
            ),

        "recommendations":
            recommendations
    }