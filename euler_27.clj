(ns euler)

(defn divisible? [n x] (= 0 (mod n x)))

(defn prime-with? [n s]
  (not-any? #(divisible? n %) s))

(defn prime-gen
  ([] (lazy-seq (cons 2 (prime-gen [2]))))
  ([s]
     (loop [x (+ 1 (last s))]
       (if (prime-with? x s)
         (let [new-primes (conj s x)]
           (lazy-seq (cons x (prime-gen new-primes))))
         (recur (+ x 1))))))

(def primes (prime-gen))

(defn prime? [n]
  (if (<= n 1) false
      (let [max-prime (Math/ceil (Math/sqrt n))]
        (loop [p primes]
          (let [x (first p)]
            (cond (and (not= n x) (divisible? n x)) false
                  (> x max-prime) true
                  :else (recur (rest p))))))))

(defn quadratic [a b c n]
  (+ (* a (* n n)) (* b n) c))

(defn quadratic-seq
  ([a b c] (quadratic-seq a b c 0))
  ([a b c n] (lazy-seq (cons (quadratic a b c n) (quadratic-seq a b c (+ 1 n))))))

(defn prime-seq-length [s]
  (count (take-while prime? s)))

(def answer
  (sort-by
   #(% :prime-len)
   >
   (for [b (range -999 1000)
         c (range -999 1000)
         :let [prime-len (prime-seq-length (quadratic-seq 1 b c))]
         :when (< 0 prime-len)]
     {:prime-len prime-len :coeff-product (* b c)})))