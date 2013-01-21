(ns cleuler.p31)

(defn ways-raw [nleft configspace] 
  (cond 
   (< nleft 0) 0
   (== nleft 0) 1
   (or (empty? configspace) (nil? configspace)) 0
   :else
   (let [curconfig (first configspace)
	     nextconfig (rest configspace)]
     (let [s
           (reduce + 
            (for [n (range 0 (+ 1 (/ nleft curconfig)))]
       		 (ways (- nleft (* n curconfig)) nextconfig)))]
       (if (nil? s) 0 s)))))

(def ways (memoize ways-raw))

(def problem-configspace [200 100 50 20 10 5 2 1])

(def starting-count 200)