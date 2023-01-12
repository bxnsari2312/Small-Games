;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname waterloo2-poker) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;;a)
;;(ordinality card) consumes card c and produces ordinaility of c
;; Examples:
(check-expect (ordinality (cons 'J (cons 'S empty))) 11)
(check-expect (ordinality (cons 'Q (cons 'D empty))) 12)
(check-expect (ordinality (cons 'K (cons 'D empty))) 13)
(check-expect (ordinality (cons 'A (cons 'D empty))) 14)
;; ordinality: listof X -> int
(define (ordinality card)
  (cond
    [(integer? (first card))
     (first card)]
    [(symbol=? (first card) 'J) 11]
    [(symbol=? (first card) 'Q) 12]
    [(symbol=? (first card) 'K) 13]
    [(symbol=? (first card) 'A) 14]))
;; Tests:
(check-expect (ordinality (cons 2 (cons 'D empty))) 2)
(check-expect (ordinality (cons 4 (cons 'D empty))) 4)

;;b)
;;(strength) consumes a hand and produces strength of hand
;;Examples:
(check-expect (strength  (cons (cons 'Q (cons 'S empty))
                               (cons (cons 'K (cons 'D empty)) empty))) 2)
(check-expect (strength (cons (cons 3 (cons 'C empty))
                              (cons (cons 'J (cons 'C empty)) empty))) 1)
(check-expect (strength  (cons (cons 'Q (cons 'C empty))
                               (cons (cons 'J (cons 'C empty)) empty))) 4)
(check-expect (strength  (cons (cons 'J (cons 'S empty))
                               (cons (cons 'J (cons 'D empty)) empty))) 3)
;; strength: listof X -> int 
(define (strength Hand)
  (cond
    [(and (symbol=? (first(rest(first Hand))) (first(rest(first(rest Hand)))))      
          (= 1 (abs (- (ordinality (first (rest Hand))) (ordinality(first Hand)))))) 4]
    [(= (ordinality (first (rest Hand))) (ordinality(first Hand))) 3]
    [(symbol=? (first(rest(first Hand))) (first(rest(first(rest Hand))))) 1]
    [(= 1 (abs (- (ordinality (first (rest Hand))) (ordinality(first Hand))))) 2]
    [else 0]))
;;Tests:
(check-expect (strength  (cons (cons 'J (cons 'S empty))
                               (cons (cons 'K (cons 'C empty)) empty))) 0)
;;c)
;;(hand<?) consumes two hands and produces true if h2 is better hand
;;Examples:
(check-expect (hand<? (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))
                      (cons (cons 'J (cons 'H empty))
                            (cons (cons 10 (cons 'H empty)) empty))) true)
(check-expect (hand<? (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))
                      (cons (cons 3 (cons 'H empty))
                            (cons (cons 'J (cons 'H empty)) empty))) false)
;;hand<?: listof X listof X -> bool
(define (hand<? h1 h2)
  (cond
    [(> (strength h2) (strength h1)) true]
    [else false]))
;;Tests:
(check-expect (hand<? (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))
                      (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))) false)

;;d)
;;(winner) consumes two hands and outputs the better hand, else gives tie
;;Examples:
(check-expect (winner (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))
                      (cons (cons 'J (cons 'H empty))
                            (cons (cons 10 (cons 'H empty)) empty))) 'hand2)
(check-expect (winner (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))
                      (cons (cons 3 (cons 'H empty))
                            (cons (cons 'J (cons 'H empty)) empty))) 'hand1)
;;winner: listof X listof X -> sym
(define (winner h1 h2)
  (cond
    [(> (strength h2) (strength h1)) 'hand2]
    [(< (strength h2) (strength h1)) 'hand1]
    [else 'tie]))
;;Tests:
(check-expect (winner (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))
                      (cons (cons 'J (cons 'S empty))
                            (cons (cons 'Q (cons 'D empty)) empty))) 'tie)

;;e)
;;(valid-card) checks if the card is valid 
;;Examples:
(check-expect (valid-card (cons 'Q (cons 'S empty))) true)
;;valid-card: Any -> bool
(define (valid-card card)
  (cond
    [(and
      (or (symbol=? 'C (first(rest card))) (symbol=? 'D (first(rest card)))
          (symbol=? 'H (first(rest card))) (symbol=? 'S (first(rest card))))

      (or (= 2 (ordinality card)) (= 3 (ordinality card))
          (= 4 (ordinality card)) (= 5 (ordinality card))
          (= 6 (ordinality card)) (= 7 (ordinality card))
          (= 8 (ordinality card)) (= 9 (ordinality card))
          (= 10 (ordinality card)) (= 12 (ordinality card))
          (= 13 (ordinality card)) (= 14 (ordinality card)))) true]
    [else false]))
;;Test:
(check-expect (valid-card (cons 10 (cons 'S empty))) true)
(check-expect (valid-card (cons 'J (cons 'A empty))) false)

;;(valid-hand) checks if hand is valid by considering
;       if the cards are valid, not same, non-empty lst
;;Examples:
(check-expect (valid-hand?(cons (cons 'Q (cons 'S empty))
                          (cons (cons 'Q (cons 'S empty)) empty))) false)
;;valid-hand: Any -> bool 
(define (valid-hand? h)
  (cond
    [(and (list? h) (= 2(length h)))
     (cond
       [(and (= (ordinality (first (rest h))) (ordinality(first h)))
             (symbol=? (first(rest(first h)))
                       (first(rest(first(rest h))))))
             false]
       [(and (valid-card (first h)) (valid-card (first(rest h)))) true]
       [else false])]
    [else false]))
;;Tests:
(check-expect (valid-hand? (cons (cons 'Q (cons 'S empty)) empty)) false)
(check-expect (valid-hand? 0) false)
(check-expect (valid-hand?(cons (cons 'Q (cons 'B empty))
                          (cons (cons 'A (cons 'F empty)) empty))) false)
(check-expect (valid-hand?(cons (cons 12 (cons 'Q empty))
                          (cons (cons 'A (cons 'Q empty)) empty))) false)
(check-expect (valid-hand?(cons (cons 'A (cons 'S empty))
                          (cons (cons 'Q (cons 'S empty)) empty))) true)
(check-expect (valid-hand?(cons (cons 2 (cons 'S empty))
                          (cons (cons 'Q (cons 'S empty)) empty))) true)
