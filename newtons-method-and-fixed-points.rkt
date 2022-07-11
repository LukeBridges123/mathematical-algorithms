#lang scheme
(define (newton-root f precision (guess 1.0))
  (if (< (abs (f guess)) precision)
      guess
      (newton-root f precision (improve f guess))))

(define (improve f old-guess)
  (- old-guess (/ (f old-guess)
                  ((derivative f) old-guess))))

(define (derivative f) ;returns a function that computes an approximation of the derivative of f at x
  (define h 0.00001)
  (lambda (x)
    (/ (- (f (+ x h)) (f x))
       h)))
;convert a polynomial represented as lists of terms, where a term is a pair (coeff degree) (e.g. x^2 - 4 is represented as ((1 2) (-4 0))), into a function that evaluates that polynomial with
;a particular number given for x.
(define (make-polynomial coeff-list) 
  (lambda (x)
    (define (eval-poly-term poly-term) (* (car poly-term)
                                          (expt x (second poly-term))))
    (foldl + 0 (map eval-poly-term coeff-list))))
;version of Newton's method that, instead of terminating when f(guess) is within a certain tolerance of 0, terminates when the difference between the previous guess and current guess is smaller
;than a certain fraction of the previous guess. In other words, terminates based on whether the change between successive guesses is a small fraction of the previous guess, the idea being that
;far from a root, the "improve" function will change guesses by a lot, while near a root, it will only change guesses a little.
(define (sliding-newton-root f precision (old-guess 1.0))
  (let ((new-guess (improve f old-guess)))
    (if (< (abs (- new-guess old-guess))
           (* old-guess precision))
        new-guess
        (sliding-newton-root f precision new-guess))))

;(newton-root (lambda (x) (- (* x x) 4)) 0.001)
;((make-polynomial '((1 2) (-4 0))) 2)
;(sliding-newton-root (make-polynomial '((1 2) (-0.000001 0))) 0.0001)
;(newton-root (make-polynomial '((1 2) (-0.000001 0))) 0.0001)
;(newton-root (make-polynomial '((1 2) (-2 0))) 0.000000000001)
;(sliding-newton-root (make-polynomial '((1 2) (-2 0))) 0.000000000001)
;(* 2 (newton-root cos 0.0000001))

;finds a fixed point of a numerical function, i.e. a value x such that f(x) = x. Assumes that the fixed points will be "attracting", i.e. that for values y close to x, f(f(y)) will be closer to
;x than f(y). This means that we can search for fixed points by starting with an arbitrary number y as an initial guess, then calculating the sequence f(y), f(f(y)), f(f(f(y))), etc. until we find
;two elements of the sequence that are close to each other (i.e. abs value of their difference is within a predetermined tolerance); when two such elements are found, we have found an x such that
;f(x) is very close to x, which means that x is approximately a fixed point of f.
(define (fixed-point f precision (first-guess 1.0))
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) precision))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next) next
          (try next))))
  (try first-guess))

(fixed-point cos 0.00001)
;golden ratio is a fixed point of the function f(x) = 1 + (1/x)
(fixed-point (lambda (x) (+ 1 (/ 1 x))) 0.000001 1.0)

;square roots as a fixed-point search: if y is a square root of x, then y is a fixed point of the function f(y) = x/y. We can't directly turn this into a fixed-point search (i.e. one whose
;function is (lambda (y) (/ x y))), because it will always get stuck in a loop: if y0 is our intial guess, then f(y0) = x/y0, and f(f(y0)) = x/f(y0) = x/(x/y0)) = y0, so we end up where we
;started. To fix this, note that if y is larger than the square root, x/y will be smaller than the square root, and vice versa if y is smaller than the square root. This means that, given a wrong
;guess, the square root is between x and x/y, so iteratively taking the average of y and x/y should bring us closer to the square root. Furthermore, if y is the real square root, then it is a
;fixed point of the function f(y) = (y + x/y)/2, since if x/y = y, then f(y) = (y + x/y)/2 = (y+y)/2 = y. This means that we can put the "average damped" version of the square-root transform,
;(lambda (y) (average y (/ x y)), into our fixed point search to find square roots.

(define (average x y) (/ (+ x y) 2))
;returns the average-damped version of a function, i.e. the function that takes in a number x and returns the average of x and f(x).
(define (average-damp f)
  (lambda (x) (average x (f x))))
(define (sqrt x)
  (fixed-point (average-damp (lambda (y) (/ x y))) 0.00001))

(sqrt 2)
(sqrt 4)
(sqrt 100)

;Newton's method is a fixed-point search: if x is a root of f, then x is a fixed point of the function g(x) = x - (f(x)/f'(x)), since if f(x) = 0, f(x)/f'(x) will also equal 0, so g(x) will just
;evaluate to x. We can think of g as the result of applying some higher-order function, "newton-transform", to f. This means that Newton's method is not just a fixed-point search, but a
;specific kind of fixed-point search: one that takes in a function and a transformation, and searches for fixed points of the transformed function. This leads to the possibility of expressing
;Newton's method as below, using the abstract "fixed-point-of-transform" function.

(define (fixed-point-of-transform transform f precision (guess 1.0))
  (fixed-point (transform f) precision guess))

(define (fixed-point-newton-root f precision (guess 1.0))
  (define (newton-transform f)
    (lambda (x)
      (- x (/ (f x)
              ((derivative f) x)))))
  (fixed-point-of-transform newton-transform f precision guess))
(newton-root (make-polynomial '((1 2) (-2 0))) 0.000001)
(fixed-point-newton-root (make-polynomial '((1 2) (-2 0))) 0.000001)