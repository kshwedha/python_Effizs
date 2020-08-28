#fastest fourier transform

F fft(x)
   V n = x.len
   I n <= 1
      R x
   V even = fft(x[(0..).step(2)])
   V odd  = fft(x[(1..).step(2)])
   V t = (0 .< n I/ 2).map(k -> exp(-2i * math:pi * k / @n) * @odd[k])
   R (0 .< n I/ 2).map(k -> @even[k] + @t[k]) [+]
     (0 .< n I/ 2).map(k -> @even[k] - @t[k])
 
print(fft([Complex(1.0), 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]).map(f -> ‘#1.3’.format(abs(f))).join(‘ ’))
