<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        .nav-user {
            color: blue;
        }
    </style>
</head>

<body>
    <h1>XIN CHÀO</h1>
    <?php
    include "includes/db_con.php";
    ?>
    <h3><a href="./admin/views/home.php">Trang admin</a></h3>
    <h3><a href="./index.php">Trang user</a></h3>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <h1 class="nav-user">Trang Người Dùng</h1>
                <h3>Các chủ đề trò chuyện có sẵn</h3>
                <?php
                include "client/all_intents.php";
                ?>
            </div>
            <div class="col-md-6">
                <h3>Thêm chủ đề mới </h3>
                <form method="post" action="client/add_intent.php">
                    <div class="form-group">
                        <label for="intentName">Tên Intent (chủ đề cuộc trò chuyện)</label>
                        <input type="text" class="form-control" id="intentName" name="intentName"
                            placeholder="Nhập chủ đề" required>
                    </div>

                    <button type="submit" class="btn btn-primary">Thêm mới</button>

                </form>
            </div>
        </div>
    </div>
    <?php
    require_once "bot.php";
    ?>


</body>

</html>