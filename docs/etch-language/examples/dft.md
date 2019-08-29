``` c++
function main()

	var inreal = Array<Fixed64>(1000);
	var inimag = Array<Fixed64>(1000);
	var outreal = Array<Fixed64>(1000);
	var outimag = Array<Fixed64>(1000);

 	for (i in 0:inreal.count())

 		inreal[i] = toFixed64(rand(0, 1000));
 		inimag[i] = toFixed64(rand(0, 1000));

 	endfor

 	dft(inreal, inimag, outreal, outimag);

 	//printLn(inreal);
 	//printLn(inimag);
 	//printLn(outreal);
 	//printLn(outimag);

endfunction


function dft(inreal : Array<Fixed64>, inimag : Array<Fixed64>, outreal : Array<Fixed64>, outimag : Array<Fixed64>)

	var n = inreal.count();
	var angle = 0.0fp64;

	for (k in 0:n)

		var sumreal = 0.0fp64;
		var sumimag = 0.0fp64;

		for (t in 0:n)

			angle = 2.0fp64 * 3.142fp64 * toFixed64(t) * toFixed64(k) / toFixed64(n);

			sumreal += inreal[t] * cos(angle) + inimag[t] * sin(angle);
			sumimag += -inreal[t] * sin(angle) + inimag[t] * cos(angle);

		endfor

		outreal[k] = sumreal;
		outimag[k] = sumimag;

	endfor

endfunction

```