""" First API; local only """
import hug

import mymalaya


@hug.cli()
@hug.get(examples='name=Bob&age=10')
@hug.local()
def hello_world(name: hug.types.text, age: hug.types.number, hug_timer=100):
    """Says goodbye world!!"""
    mymalaya.test_preprocess()
    return {"message": "Goodbye {0} World!! {1}! Sib!!!".format(age, name),
            "took": float(hug_timer)}
