from statistics import median
from django.db.models import (
    Avg,
    Count,
    Variance,
    Max,
    Min,
)
from django.contrib.postgres.aggregates import ArrayAgg
from app.pokeapi.models import Berry
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample


@extend_schema(description="""Poke Berries Statistics API""")
class BerryViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        result = Berry.objects.aggregate(
            berries_names=ArrayAgg("name"),
            min_growth_time=Min("growth_time"),
            median_growth_time=ArrayAgg("growth_time"),
            max_growth_time=Max("growth_time"),
            variance_growth_time=Variance("growth_time"),
            mean_growth_time=Avg("growth_time"),
        )
        frequency_growth_time = dict(
            frequency_growth_time=dict(
                Berry.objects.values_list("growth_time").annotate(
                    frequency=Count("growth_time")
                )
            )
        )
        result["median_growth_time"] = median(result["median_growth_time"])
        response = {**result, **frequency_growth_time}
        return Response(response)
