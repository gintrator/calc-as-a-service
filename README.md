# Calculator as a Service

It's in the name. There is one endpoint, `/equals`. There are 3 required parameters: x, y, and op. Results are returned as JSON. If everything went smoothly, a "result" field will hold the result as a float, or, if something bad happened, an "error" field with a helpful description of what went wrong. 

So, if you're thinking, 1 + 2 equals...? Just fire off a quick post request.

`POST http://localhost/equals?x=1&y=2&op=add`

There's a test script included called `test_caas.sh`. It accepts command line arguments as follows. `$ test_caas.sh 1 2 add` to do the post request above.

Addition is offered a free service. For additional operations, such as subtraction, multiplication, and division, look into an enterprise license. 
