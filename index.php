<!-- SELECT i.intent_name,e.example_question,a.chat_answer FROM `intents` i JOIN example_intent e on i.intent_id=e.intent_id JOIN answer_intent a on i.intent_id = a.intent_id  -->

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
    <h3><a href="./admin/views/home.php">Trang admin</a></h3>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <h2>Trang Ngừi Dùng</h2>
                <h3>Các intent có sẵn</h3>
                <?php
                include "all_intents.php";
                ?>
            </div>
            <div class="col-md-6">
                <h3>Thêm intent mới</h3>
                <form method="post" action="add_intent.php">
                    <div class="form-group">
                        <label for="intentName">Tên Intent (chủ đề cuộc trò chuyện)</label>
                        <input type="text" class="form-control" id="intentName" name="intentName"
                            placeholder="Nhập chủ đề" required>
                    </div>
                    <!-- <div class="form-group">
                        <label for="description">Câu hỏi liên quan đến chủ đề này</label>
                        <textarea class="form-control" id="question" name="question" placeholder="Nhập câu hỏi" rows="3"
                            required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="answer">Câu trả lời cho chủ đề trên</label>
                        <textarea class="form-control" id="answer" name="answer" placeholder="Nhập câu trả lời" rows="3"></textarea>
                    </div> -->

                    <button type="submit" class="btn btn-primary">Thêm mới</button>
                    <!-- <a class="btn btn-secondary" href="ghi_file.php">ghi file</a>
                    <form method="post" action="train_rasa.php">
                        <input type="submit" name="train_rasa" class="btn btn-warning" value="Train Rasa">
                    </form>
                    <form method="post" action="stop_rasa.php">
                        <input type="submit" name="train_rasa" class="btn btn-danger" value="Stop Rasa">
                    </form> -->
                </form>
            </div>
        </div>
    </div>

    

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