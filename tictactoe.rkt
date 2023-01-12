;;(count-row row symb) produces the number of element produces in the row

;;Example:
(check-expect (count-row (list 'O 'X 'O) 'O)2)
(define (count-row row symb)
  (cond
    [(empty? row) 0]
    [(symbol=? (first row) symb)
     (+ 1 (count-row (rest row) symb))]
    [else (count-row (rest row) symb)]
    ))
;;(grid-count grids symb) produces the number of elements in the total grid

;;Example:
(check-expect (grid-count
               (list (list '_ '_ '_)
                    (list '_ '_ '_)
                    (list '_ '_ '_)) 'X)0)

(define (grid-count grids symb)
  (cond
    [(empty? grids) 0]
    [else
     (+ (count-row (first grids) symb)
        (grid-count (rest grids) symb))]
    ))

;;(whose-turn grid) produces whether it should be player X or
;;player O's turn

;;Example:
(check-expect (whose-turn (list (list 'X 'O '_)
                    (list '_ '_ '_)
                    (list '_ '_ '_)))'X)

;;whose-turn: T3Grid -> (anyof 'X 'O)
;; A Tic-Tac-Toe Grid (T3Grid) is a (listof (listof (anyof 'X 'O '_)))
;; Requires: all lists have the same length, and that length is odd
;; The number of 'X and 'O is equal, or there is one more 'X
(define (whose-turn grid)
  (cond
    [(empty? grid) 0]
    [(= (grid-count grid 'X)(grid-count grid 'O)) 'X]
    [else 'O]))

;;Tests:
(check-expect (whose-turn (list (list 'X 'O '_)
                    (list '_ 'X '_)
                    (list '_ '_ '_)))'O)
(check-expect (whose-turn (list (list 'X 'O 'O)
                    (list '_ '_ 'X)
                    (list '_ '_ '_)))'X)
(check-expect (whose-turn (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list '_ '_ '_)))'O)

;;b)
;;(grid-ref grid row col) produces  the symbol located at that location
;; of specific row and column number

;;Example:
(check-expect (grid-ref (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list '_ '_ '_)) 0 1)'O)
(define (grid-ref grid row col)
  (cond
    [(empty? grid) grid]
    [else (list-ref (list-ref grid row) col)]
    ))

;;Tests:
(check-expect (grid-ref (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list '_ '_ '_)) 0 1)'O)
(check-expect (grid-ref (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list '_ '_ '_)) 0 2)'_)
(check-expect (grid-ref (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_)) 2 0)'X)
;;c)
;;(get-column grid col) produces a list of the symbols in that column
;;of column number 

;;Example:
(check-expect (get-column (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_))0) (list 'X '_ 'X))

;;get-column: T3Grid Nat -> (listof (anyof 'X 'O '_))
;; A Tic-Tac-Toe Grid (T3Grid) is a (listof (listof (anyof 'X 'O '_)))
;; Requires: all lists have the same length, and that length is odd
;; The number of 'X and 'O is equal, or there is one more 'X
(define (get-column grid col) 
  (cond
    [(empty? grid) empty]
    [else (cons (list-ref (first grid) col)
          (get-column (rest grid) col))]))

;;Tests:
(check-expect (get-column (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_))0) (list 'X '_ 'X))
(check-expect (get-column (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_))1) (list 'O '_ '_))
(check-expect (get-column (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_))2) (list '_ 'X '_))
(check-expect (get-column (list (list 'X 'O )
                    (list '_ '_ )
                    )0) (list 'X '_ ))
;;d)
;;(will-win? grid row col player) produces whether the player will win
;;if he put the marker at specific column number and row number

;;Example:
(check-expect (will-win? (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_))0 2 'X)false)
;;will-win?
(define (will-win? grid row col player)
  (cond
    [(empty? grid) false]
    [(not (symbol=? (grid-ref grid row col) '_))
     false]
    [(= 1 (- (length grid)(count-row (get-column grid col) player)))
     true]
    [(= 1 (- (length grid)(count-row (list-ref grid row) player)))
     true]
    [else false]
    ))

;;Tests:
(check-expect (will-win? (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_))1 0 'X)true)
(check-expect (will-win? (list (list 'X 'O '_)
                    (list '_ '_ 'X)
                    (list 'X '_ '_))0 1 'X)false)
(check-expect (will-win? (list (list 'X 'O '_)
                    (list '_ 'O 'X)
                    (list 'X '_ '_))2 1 'O)true)
