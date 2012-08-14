(ns euler (:use clojure.contrib.math))

(def answer
  (count
   (distinct
    (for [a (range 2N 101N) b (range 2N 101N)] (expt a b)))))