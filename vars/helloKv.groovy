// vars/helloKv.groovy
import kv.utils.Calculator

def call(String name, int first, int second) {
    def result = Calculator.add(first, second)
    echo "Result is ${result}"
    echo "Hello, ${name}!"
}

def karthik(String kv) {
    echo "HI, ${kv}"
}
