// vars/helloKv.groovy
import kv.utils.Calculator

def call(String name) {
    def result = Calculator.add(1, 2)
    echo "Result is ${result}"
    echo "Hello, ${name}!"
}

def karthik(String kv) {
    echo "HI, ${kv}"
}
