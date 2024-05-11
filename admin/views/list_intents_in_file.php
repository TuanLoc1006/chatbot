<?php
include "../../db_con.php";

$sql_intents = "SELECT DISTINCT i.intent_name,i.intent_id
FROM `intents` i 
JOIN example_intent e ON e.intent_id = i.intent_id 
JOIN answer_intent a ON a.intent_id = i.intent_id 
WHERE  e.status_file = '1' or a.status_file = '1'";
$result = $conn->query($sql_intents);

if ($result && $result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $intent_id = $row['intent_id'];
        $intent_name = $row['intent_name'];
        ?>
        <div class="card">
            <a href="intent_detail_in_file.php?intent_id=<?php echo $intent_id; ?>" class="card-link">
                <div class="card-body">
                    <h5 class="card-title"><?php echo $intent_name; ?></h5>
                    <input type="submit" name="" hidden value="<?php echo $intent_id ?>">
                </div>
            </a>
            <form method="post" action="del_data_nlu_domain_stories.php" onsubmit="return confirmDelete();">
                <input type="hidden" name="intent_id" value="<?php echo $intent_id ?>">
                <input type="hidden" name="intent_name" value="<?php echo $intent_name ?>">
                <input type="submit" class="btn btn-danger" value="Xoa" name="delete_intent">
            </form>
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