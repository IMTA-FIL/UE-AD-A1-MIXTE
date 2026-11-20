from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from flask import Flask, request, jsonify

import resolvers as r

PORT = 3001
HOST = '0.0.0.0'
app = Flask(__name__)

type_defs = load_schema_from_path("movie.graphql")
query = QueryType()
mutation = MutationType()
movie = ObjectType("Movie")
actor = ObjectType("Actor")
query.set_field("movie_with_id", r.movie_with_id)
mutation.set_field("update_movie_rate", r.update_movie_rate)
mutation.set_field("add_movie", r.add_movie)
movie.set_field("actors", r.resolve_actors_in_movie)
schema = make_executable_schema(type_defs, movie, query, mutation, actor)

# graphql entry points
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, debug=app.debug)
    return jsonify(result), 200 if success else 400

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)