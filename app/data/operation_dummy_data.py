from models import Operation
from uuid import UUID, uuid4
from typing import List


db: List[Operation] = [
 Operation(     
   id = "0725f377-11d4-4f09-a7bf-e292ae783c11",
   amount_required = 100,
   amount_limit = 1000,
   interest_rate = 0.152,
   date_deadline = "2024-11-17T21:34:56.756000Z",
   datetime_published = "2024-10-17T21:34:56.756000Z",
   status = "open",
   bids = [],
   creator_user_id = "3725f377-11d4-4f09-a7bf-e292ae783c11",
   inversor_user_id = "3725f377-11d4-4f09-a7bf-e292ae783c13"
 ),
 Operation(     
   id = "0725f377-11d4-4f09-a7bf-e292ae783c12",
   amount_required = 150,
   amount_limit = 800,
   interest_rate = 0.185,
   date_deadline = "2024-12-20T21:34:56.756000Z",
   datetime_published = "2024-10-17T21:34:56.756000Z",
   status = "open",
   bids = [],
   creator_user_id = "3725f377-11d4-4f09-a7bf-e292ae783c11",
   inversor_user_id = "3725f377-11d4-4f09-a7bf-e292ae783c12"
 ),
 Operation(     
   id = "0725f377-11d4-4f09-a7bf-e292ae783c13",
   amount_required = 200,
   amount_limit = 1200,
   interest_rate = 0.17,
   date_deadline = "2025-01-17T21:34:56.756000Z",
   datetime_published = "2024-10-17T21:34:56.756000Z",
   status = "closed",
   bids = [],
   creator_user_id = "3725f377-11d4-4f09-a7bf-e292ae783c11",
   inversor_user_id = "3725f377-11d4-4f09-a7bf-e292ae783c12"
 )
]