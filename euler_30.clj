(ns euler (:use clojure.contrib.math))

(defn digits [n]
  (let [digit (mod n 10)
        rest-n (int (/ n 10))]
    (if (= rest-n 0)
      [digit]
      (conj (digits rest-n) digit))))

(defn digits-to-num [ds]
  (let [dsr (reverse ds)]
    (reduce +
            (for [e (range 0 (count dsr))
                  :let [d (nth dsr e)]]
              (* (bigint d) (expt 10 e))))))
                  

(defn digit-pow-sum [n p]
  (reduce + (map #(int (expt % p)) (digits n))))

(def max-num-digits
  ;; account for both 1 digit, which we are skipping, and the last digit,
  ;; which we don't see in the for loop because the while returns one step
  ;; early.
  (+ 2  
     (count
      (for [d (range 2 100)
            :let [n (digits-to-num (repeat d 9))]
            :while (>= (digit-pow-sum n 5) n)]
        d))))

(def answer
  (reduce +
          (for [i (range 10 (+ 1 (digits-to-num (repeat max-num-digits 9))))
                :when (= i (digit-pow-sum i 5))]
            i)))