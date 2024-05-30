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
    <?php
    include "includes/db_con.php";
    ?>
    <!-- <h3><a href="./admin/views/home.php">Trang admin</a></h3> -->
    <h3><a href="./index.php">Trang user</a></h3>
    <!-- <div class="container">
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
    </div> -->
    <?php
    require_once "bot.php";
    ?>

    <!-- 
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
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