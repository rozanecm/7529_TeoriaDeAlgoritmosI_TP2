(defn bruteforce [s, w]
    (if (= s w) 
        true
        (
            (defn bruteforce_in [s_in, w_in]
                (if (= original_w w_in) 
                    false
                    (if (= s_in w_in) 
                        true
                        (bruteforce_in s_in (str (subs w_in 1) (str (get w_in 0))))
                    )
                )
            )
            (bruteforce_in s (str (subs w 1) (str (get w 0))))
        )
    )
)

(defn ARGV [n] (nth *command-line-args* n))
(println (bruteforce (ARGV 0) (ARGV 1)))
