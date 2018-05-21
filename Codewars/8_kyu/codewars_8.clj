; https://www.codewars.com/kata/even-or-odd/train/clojure
(defn even-or-odd [number]
  (if (odd? number ) "Odd" "Even")
)

; https://www.codewars.com/kata/how-many-lightsabers-do-you-own/train/clojure
(defn howManyLightsabersDoYouOwn [name] (if (= name "Zach") 18 0))