<?php
// include "includes/db_con.php";

$sql_intents = "SELECT `intent_id`, `intent_name`, `status_file` FROM `intents`";
$result = $conn->query($sql_intents);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intent List</title>
    <style>
        .scroll-container {
            max-height: 600px; /* Set the max height for the scrollable area */
            overflow-y: auto; /* Enable vertical scrolling */
            border: 1px solid #ddd; /* Optional: Add a border for better visualization */
            padding: 10px; /* Optional: Add padding */
        }
        .card {
            margin-bottom: 10px; /* Space between cards */
            border: 1px solid #ccc; /* Card border */
            padding: 10px; /* Card padding */
        }
        .card-link {
            text-decoration: none; /* Remove underline from links */
            color: inherit; /* Inherit color */
        }
        .card-body {
            padding: 10px; /* Padding inside card body */
        }
        .text-success {
            color: green; /* Success text color */
        }
        .text-danger {
            color: red; /* Danger text color */
        }
        .btn-danger {
            background-color: red; /* Danger button background color */
            color: white; /* Danger button text color */
            border: none; /* Remove border */
            padding: 10px 20px; /* Button padding */
            cursor: pointer; /* Pointer cursor on hover */
        }
    </style>
</head>
<body>
    <div class="scroll-container">
        <?php
        if ($result && $result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                $intent_id = $row['intent_id'];
                $intent_name = $row['intent_name'];
                $status_file = $row['status_file'];
                ?>
                <div class="card">
                    <a href="client/intent_details.php?intent_id=<?php echo $intent_id; ?>" class="card-link">
                        <div class="card-body">
                            <h5 class="card-title"><?php echo $intent_name; ?></h5>
                            <?php if ($status_file == 1) { ?>
                                <p class="text-success">Đã ghi file</p>
                            <?php } else { ?>
                                <p class="text-danger">Chưa ghi file</p>
                            <?php } ?>
                            <input type="submit" name="" hidden value="<?php echo $intent_id ?>">
                        </div>
                    </a>
                    <?php if ($status_file == 0) { ?> <!-- Kiểm tra status_file -->
                        <form method="post" action="client/delete_intent.php" onsubmit="return confirmDelete();">
                            <input type="hidden" name="intent_id" value="<?php echo $intent_id ?>">
                            <input type="submit" class="btn btn-danger" value="Xóa chủ đề" name="delete_intent">
                        </form>
                    <?php } ?>
                </div>

                <script>
                    function confirmDelete() {
                        return confirm("Bạn có chắc chắn muốn xóa?");
                    }
                </script>

                <?php
            }
        } else {
            echo "Không có chủ đề nào được tìm thấy.";
        }
        ?>
    </div>
</body>
</html>
