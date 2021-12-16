fun main() {
    println("Hello, World!")
}

main()

val num = 7

for (i in 1..num) {
    println(i)
}

var a = 3
// simple name in template:
val s1 = "a is $a"

a = 2
// arbitrary expression in template:
val s2 = "${s1.replace("is", "was")}, but now is $a"
println(s2)

fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }

describe("un saludo")

fun calculoraro(num: Int) :Int =
    when (num) {
        1   -> 1*2
        2   -> {
                  val res= num+2
                  res*3
               }
        3   -> 3*2
        else -> 0
    }

println(calculoraro(1))
println(calculoraro(2))
println(calculoraro(3))

for (i in 1..10) { println(i)}
