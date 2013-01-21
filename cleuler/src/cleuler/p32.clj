(ns cleuler.p32)

(def all-pairs
  (for [x (range 10 100)
        y (range 10 100)
        :when (< x y)]
    [x y]))

(defn common-factors [initial-x initial-y]
  (loop [x initial-x y initial-y primes primes acc (list)]
    (if (nil? primes) acc
    (let [p (first primes)]
      (println x y p (take 5 primes))
      (if (or (empty? primes) (nil? primes) (and (> p initial-x) (> p initial-y))) acc
        (let [is-factor (and (== (mod x p) 0) (== (mod y p) 0))
              next-x (if is-factor (/ x p) x)
              next-y (if is-factor (/ y p) y)
              next-primes (if is-factor primes (rest primes))
              next-acc (if is-factor (cons p acc) acc)]
          (recur next-x next-y next-primes next-acc)))))))

(def primes (sieve (range 2 99)))

(defn sieve [s]
  ;; From the clojure cheat sheet.
  (cons (first s)
        (lazy-seq (sieve (filter #(not= 0 (mod % (first s)))
                                 (rest s))))))