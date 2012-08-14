(ns euler)

(defn square [n] (* n n))

(defn square-corners [edge-length]
  (let [last-edge-length (max 0 (- edge-length 2))
        starting-line (+ 1 (square last-edge-length) last-edge-length)
        ending-line (+ 1 (square edge-length))]
    (range starting-line ending-line (+ 1 last-edge-length))))

(defn diag-seq [n]
  (assert (odd? n))
  (flatten
    (for [side-length (range 1 (+ n 1) 2)]
      (square-corners side-length))))

(def answer (reduce + (diag-seq 1001)))