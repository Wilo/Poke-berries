from typing import List, Dict

try:
    from gql import Client
    from gql import gql as Query
    from gql.transport.exceptions import (
        TransportError,
        TransportQueryError,
    )
    from gql.transport.requests import RequestsHTTPTransport
except ImportError:
    raise ImportError("Please install gql!")

from environ import ImproperlyConfigured
from config.settings.base import env


def get_data(query: str) -> List[Dict]:
    """ """
    try:
        API_URL: str = env.str("POKEAPI_API_URL")
        # Select your transport with a defined url endpoint
        transport = RequestsHTTPTransport(
            url=API_URL,
            verify=True,
            retries=3,
        )
        # Create a GraphQL client using the defined transport
        client = Client(transport=transport, fetch_schema_from_transport=False)
        # Provide a GraphQL query
        q = Query(query)
        # Execute the query on the transport
        response = client.execute(q)
    except ImproperlyConfigured:
        raise ImproperlyConfigured("Please, Set the API_URL environment variable!")
    except (TransportError) as ex:
        raise ex("Connection Error!")
    except TransportQueryError:
        raise TransportQueryError("Query Error!")
    return response.get("berries")
