
;;a)
;;(both DL1 DL2) consumes two DL and produces DL that that occurr in both DL
;;Examples:
(check-expect (both (list "a.txt") (list "a.txt" "b.txt"))  (list "a.txt"))
(check-expect (both (list "c.txt") (list "c.txt")) (list "c.txt"))
;;both: (listof Str) (listof Str) -> (listof Str)
(define (both DL1 DL2)
  (cond
    [(or (empty? DL1) (empty? DL2)) empty]
    [(string=? (first DL1)(first DL2))
     (cons (first DL1)(both DL1 (rest DL2)))]
    [(string<? (first DL1) (first DL2))  
     (both (rest DL1) DL2)]
    [else (both DL1 (rest DL2))]
    ))
;;Tests:
(check-expect (both (list "b.txt") (list "c.txt")) empty)
(check-expect (both (list "c.txt") (list "a.txt")) empty)
(check-expect (both (list "a.txt") (list "a.txt")) (list "a.txt"))
(check-expect (both (list "c.txt" "b.text") (list "c.txt")) (list "c.txt"))

;;b)
;;(exclude DL1 DL2) consumes two DL and produces DL that occur in first but not second
;;Examples:
(check-expect (exclude (list "b.txt" "c.txt") (list "b.txt"))  (list "c.txt"))
(check-expect (exclude (list "a.txt" "b.txt") (list "b.txt" "c.txt"))  (list "a.txt")) 
;;exclude: (listof Str) (listof Str) -> (listof Str) 
(define (exclude DL1 DL2)  
  (cond
    [(empty? DL1) empty] 
    [(empty? DL2) DL1] 
    [(string<? (first DL1) (first DL2))
     (cons (first DL1)(exclude (rest DL1) DL2))]
    [(string>? (first DL1) (first DL2))
     (exclude DL1 (rest DL2))]
    [(string=? (first DL2) (first DL1)) (exclude (rest DL1) (rest DL2))]
    [else DL1]
    ))
;;Tests:
(check-expect (exclude (list "a.txt") (list "a.txt")) empty)
(check-expect (exclude (list "b.txt" "d.txt") (list "b.txt"))  (list "d.txt"))
(check-expect (exclude (list "d.txt" "e.txt") (list "b.txt" "c.txt"))  (list "d.txt" "e.txt"))

;;c)
;;(keys-retrieve doc an-il) consumes a str and IL, checks the second element
;; to see if it has doc, if it does, then it cons the first element 
;;Examples:
(check-expect(keys-retrieve "b.txt"
                            (list
                             (list "bed" (list "b.txt"))
                       (list "desk" (list "a.txt" "c.txt"))
                       (list "elegant" (list "c.txt")))) (list "bed"))
;;keys-retrieve: Str AL -> (listof Str) 
(define (keys-retrieve doc an-il)
  (cond
    [(empty? an-il) empty]
    [(cons? (both (list doc)
                  (second (first an-il))))
     (cons (first (first an-il))(keys-retrieve doc (rest an-il)))] 
    [else (keys-retrieve doc (rest an-il))] 
    ))  
;;Tests:
(check-expect(keys-retrieve "b.txt"
                            (list
                             (list "bed" (list "b.txt"))
                       (list "desk" (list "a.txt" "c.txt"))
                       (list "elegant" (list "c.txt")))) (list "bed"))
(check-expect (keys-retrieve "c.txt"
                             (list
                              (list "a"(list "a.txt"))
                             (list "b"(list "b.txt"))
                             (list "c"(list "c.txt"))))
                             (list "c")) 

(check-expect(keys-retrieve "e.txt"
                            (list
                             (list "bed" (list "b.txt"))
                       (list "desk" (list "a.txt" "c.txt"))
                       (list "elegant" (list "c.txt")))) empty)

;;d)
;;(checks-IL doc lst) produces the second element of the element that we
;; are looking for in the whole association list

;;chekcs-IL: Str (listof Str) -> (listof Str)
(define (checks-IL doc lst)
  (cond
    [(empty? lst)empty]
    [(string=? doc (first (first lst)))
     (second (first lst))]
    [else (checks-IL doc (rest lst))]))

;;(search check-type val1 val2 lst) produces the result of the e documents
;; that are present in both if the check-type is 'both, and it produces the
;;e documents that are present in the doc-list associated with the key str1,
;;but not the key str2 if the check-type is 'exclude.

;;Example:
(check-expect (search 'both "a" "b"
                      (list
                              (list "a"(list "a.txt"))
                             (list "b"(list "b.txt"))
                             (list "c"(list "c.txt"))))empty)

;;search: (anyof 'both 'exclude) Str Str AL -> DL
(define (search check-type val1 val2 lst)
  (cond
    [(symbol=? 'both check-type)
     (cond
       [(empty? lst) empty]
       [(or (empty? (checks-IL val1 lst))
            (empty? (checks-IL val2 lst)))
        empty]
       [else (both (checks-IL val1 lst)
                   (checks-IL val2 lst))]
       )]
     [(symbol=? 'exclude check-type)
      (cond
        [(empty? lst) empty]
       [(or (empty? (checks-IL val1 lst))
            (empty? (checks-IL val2 lst)))
        empty]
       [else (exclude (checks-IL val1 lst)
                   (checks-IL val2 lst))]
       )])) 

;;Tests:
(check-expect (search 'both "a" "b"
                      (list
                              (list "a"(list "a.txt"))
                             (list "b"(list "b.txt"))
                             (list "c"(list "c.txt"))))empty)
(check-expect (search 'both "a" "c"
                      (list
                              (list "a"(list "a.txt"))
                             (list "b"(list "b.txt"))
                             (list "c"(list "c.txt"))))empty)
(check-expect (search 'exclude "a" "c"
                      (list
                              (list "a"(list "a.txt"))
                             (list "b"(list "b.txt"))
                             (list "c"(list "c.txt"))))(list "a.txt"))
(check-expect (search 'exclude "a" "b"
                      (list
                              (list "a"(list "a.txt"))
                             (list "b"(list "a.txt"))
                             (list "c"(list "c.txt"))))empty)
