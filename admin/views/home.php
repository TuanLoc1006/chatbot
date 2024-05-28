<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <?php
    include "../../includes/db_con.php";
    ?>
    <style>
        .nav-user {
            color: blue;
        }
    </style>
</head>

<body>
    <h3><a href="./home.php">Trang admin</a></h3>
    <h3><a href="../../index.php">Trang user</a></h3>
    <div class="container">
        <h1 class="nav-user">Trang admin</h1>
        <div class="row">
            <div class="col-md-8">
                <h2>Các chủ đề chưa ghi vào file train rasa</h2>
                <?php
                include "list_intents_not_in_file.php";
                ?>
                <h2>Các chủ đề đã ghi vào file rasa</h2>
                <?php
                include "list_intents_in_file.php";
                ?>
            </div>
            <div class="col-md-4">
                <a class="btn btn-secondary" href="../control_rasa/write_to_file.php">ghi file</a>

                <form method="post" action="../control_rasa/train_rasa.php">
                    <input type="submit" name="train_rasa" class="btn btn-warning" value="Train Rasa">
                </form>

                <form method="post" action="../control_rasa/stop_rasa.php">
                    <input type="submit" name="stop_rasa" class="btn btn-danger" value="Stop Rasa">
                </form>

                <form method="post" action="../control_rasa/run_rasa.php">
                    <input type="submit" name="run_rasa" class="btn btn-primary" value="Run Rasa">
                </form>
            </div>
        </div>
    </div>

    <!-- <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script> -->
</body>


</html>