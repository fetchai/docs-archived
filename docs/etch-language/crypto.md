<H2>SHA256</H2>

The `SHA256()` object gives you a number of ways to generate random 32 byte hashes which are returned as a 64 digit hexadecimal number.

Use `update()` on the `SHA256()` object to include `String` or `Buffer` types into the context before finalising the hash. 

The `final()` function generates the hash and returns the value. 

The `reset()` function allows you to start over with the same object.


``` c++
function main()
    
    // construct a SHA256 object
  	var s = SHA256();
  	// update the object with a string
  	s.update("hello");
  	// update the object with a Buffer
  	var buffer = Buffer(8);
  	s.update(buffer);
  	// finalise the object
  	s.final();
  	// reset the object
  	s.reset();

endfunction

```

Here's another example which builds a SHA256 hash by concatenating strings into the context object.

``` c++
function main()

    var my_string_value_1 = "sdkjfhiuwehfesdfno;s;'mADF;LK";
    var my_string_value_2 = "ipoiuwr8934jklnwlkj0892;m";
    var my_string_value_3 = "vvvowywnklhjxlmxxxxxxxxxxxxxxxxxxxxxxxxtreretrgy653wre6548";

    // create a SHA256() context object
    var sha256_hasher_context = SHA256();
    // give it your strings
    sha256_hasher_context.update(my_string_value_1);
    sha256_hasher_context.update(my_string_value_2);
    sha256_hasher_context.update(my_string_value_3);

    // finalise the context and print the hash value
    var hash_value_of_concatenated_strings_1_2_3 = sha256_hasher_context.final(); 
    printLn("Hash of my concatenated string 1,2,3 = " + toString(hash_value_of_concatenated_strings_1_2_3));

    // RESETTING context of the hasher since we want to start calculate hash from the scratch
    sha256_hasher_context.reset();
    
    // more strings
    var my_string_value_4 = "12345fg";
    var my_string_value_5 = "@!#$@#%#";
    var my_string_value_6 = "{}:>L$%^:c";

    // add to context
    sha256_hasher_context.update(my_string_value_4);
    sha256_hasher_context.update(my_string_value_5);
    sha256_hasher_context.update(my_string_value_6);
    // finalise and print the value
    var hash_value_of_concatenated_strings_4_5_6 = sha256_hasher_context.final();
    printLn("Hash of my concatenated string 4,5,6 = " + toString(hash_value_of_concatenated_strings_4_5_6));

endfunction
```

<br/>