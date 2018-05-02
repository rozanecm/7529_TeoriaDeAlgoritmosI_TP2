(defn bruteforce [s_in, w_in]
    (if (== (compare s_in w_in) 0) true
        (let [original_w w_in]
            (defn bruteforce_in [s, w]
                (if (== (compare original_w w) 0) false
                (if (== (compare s w) 0)
                    true
                    (bruteforce_in s (str (subs w 1) (str (get w 0))))
                ))
            )
            (def ww (str (subs w_in 1) (str (get w_in 0))))
            (bruteforce_in s_in ww)
        )
    )
)

(println (bruteforce "ABRACADABRA" "DABRAABRACA"))
