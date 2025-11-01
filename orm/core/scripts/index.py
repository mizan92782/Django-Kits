from django.db import connection

def run():
  with connection.cursor() as cursor:
    # টেবিলের সব ইনডেক্স লিস্ট
    cursor.execute("PRAGMA index_list('student');")
    indexes = cursor.fetchall()
    print("Indexes:", indexes)

    # যদি কোনো ইনডেক্সে ডিটেইলস দেখতে চাও
    for idx in indexes:
        index_name = idx[1]  # index_list এর 2nd column হলো name
        cursor.execute(f"PRAGMA index_info('{index_name}');")
        info = cursor.fetchall()
        print(f"Details of {index_name}:", info)