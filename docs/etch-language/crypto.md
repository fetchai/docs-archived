<H2>SHA256</H2>

`etch` supports a SHA256 object.


``` c++
function main()
    
    // construct a SHA256 object
  	var s = SHA256();
  	// update the object with a string
  	s.update("hello");
  	// update the object with a Buffer
  	var byteArray = Buffer(8);
  	s.update(byteArray);
  	// finalise the object
  	s.final();
  	// reset the object
  	s.reset();

endfunction

```


<br/>