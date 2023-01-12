;;some word games:

Game 1: 

;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname sarcasm) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;;4
;;a)
;;pair-listof-X-template: takes in a lst and processes the first two terms
;; considers the cases if the lst is either empty, one term or two terms
;;pair-listof-X-template: (listof X) -> Any
(define (pair-listof-X-template X lst)
  (cond
    [(empty? lst)...]
    [(= (length lst) 1) (...(first lst)
                            (pair-listof-X-template (rest lst)))]
    [(>= (length lst) 2) (...(first lst)
                             (second lst)
                             (pair-listof-X-template (rest (rest lst))))]
    ))


;;b)
;;(caps-char lst) converts char in list upper
;;and lowercase alternatively
;;Examples:
(check-expect (caps-char (cons #\A (cons #\A empty)))
              (cons #\A (cons #\a empty)))
(check-expect (caps-char (cons #\a (cons #\b empty)))
              (cons #\A (cons #\b empty)))
;;(caps-char) (listof Char)-> (listof Char)
(define (caps-char lst)
  (cond
    [(empty? lst) empty]
    
    [(= (length lst) 1)
     (cons (char-upcase(first lst))
     (caps-char (rest lst)))]

    [(>= (length lst) 2)
     (cons (char-upcase (first lst))
           (cons (char-downcase (first (rest lst))) 
           (caps-char (rest (rest lst)))))]
    ))
;;Tests
(check-expect (caps-char empty)
              empty)
(check-expect (caps-char empty)
              empty)
(check-expect (caps-char (cons #\b empty))
              (cons #\B empty))

;;(sarcastic phrase) takes a str and makes it upper and lowercase alternatively
;;Examples:
(check-expect (sarcastic "h") "H")
(check-expect (sarcastic "hEy") "HeY")
;;sarcastic: Str -> Str
(define (sarcastic phrase)
  (list->string (caps-char(string->list phrase))))
;;Tests:
(check-expect (sarcastic "Hello") "HeLlO")
(check-expect (sarcastic "HI THERE") "Hi tHeRe")
(check-expect (sarcastic " ") " ")
(check-expect (sarcastic "") "")

;;Game 2:

;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fizz-buzz) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;;5)
;;(fizz-buzz) considers if the game is fizz or buzz
;;Examples:
(check-expect (fizz-buzz 1 2 3 4) (cons 1 (cons 2 empty)))
(check-expect (fizz-buzz 9 10 4 5) (cons 9 (cons 'buzz empty)))
;;fizz-buzz: Int Int Nat Nat -> (listof X)
(define (fizz-buzz start end fizz buzz)
  (cond
    [(> start end) empty]
    
    [(and (= (remainder start buzz) 0)
          (= (remainder start fizz) 0))
          (cons 'honk (fizz-buzz (add1 start) end fizz buzz))]
    
    [(= (remainder start fizz) 0)
     (cons 'fizz (fizz-buzz (add1 start) end fizz buzz))]
    
    [(= (remainder start buzz) 0)
     (cons 'buzz (fizz-buzz (add1 start) end fizz buzz))]
    
    [else (cons start (fizz-buzz (add1 start) end fizz buzz))]
    ))
;;Tests:
(check-expect (fizz-buzz 5 5 4 5) (cons 'buzz empty))
(check-expect (fizz-buzz 1 1 1 1) (cons 'honk empty))
(check-expect (fizz-buzz 3 2 2 2) empty)
