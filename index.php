<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>

<body>
    <?php
    include "db_con.php";
    ?>

    <div class="container">
        <form method="post" action="save_data.php">
            <div class="form-group">
                <label for="intentName">Intent Name (chủ đề cuộc trò chuyện)</label>
                <input type="text" class="form-control" id="intentName" name="intentName"
                    placeholder="Nhập chủ đề" required>
            </div>
            <div class="form-group">
                <label for="description">Các câu hỏi liên quan đế chủ đề này</label>
                <input type="text" class="form-control" id="question" name="question" placeholder="Nhập câu hỏi"
                    required>
            </div>
            <div class="form-group">
                <label for="answer">Câu trả lời cho chủ đề trên</label>
                <input type="text" class="form-control" id="answer" name="answer" placeholder="Nhập câu trả lời"
                    >
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

        <a class="btn btn-secondary" href="ghi_file.php">ghi file</a>
        <form method="post" action="train_rasa.php">
            <input type="submit" name="train_rasa" class="btn btn-warning" value="Train Rasa">
        </form>
        <form method="post" action="stop_rasa.php">
            <input type="submit" name="train_rasa" class="btn btn-danger" value="Stop Rasa">
        </form>
    </div>
    
    <?php
    // include "chat.php";
    ?>
    <!-- <script>
    $(document).ready(function(){
        $("#trainButton").click(function(){
            $.ajax({
                type: "POST",
                url: "train_rasa.php",
                success: function(response){
                    alert(response);
                }
            });
        });
    });
    </script> -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>

<!--  Stop-Process -Name "rasa" -->