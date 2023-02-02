import justpy as jp
import definition
import json

class Api:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        defined = definition.Deffenition(word).get()

        response = {
            "word":word,
            "defenition":defined
        }

        wp.html = json.dumps(response)
        return wp

