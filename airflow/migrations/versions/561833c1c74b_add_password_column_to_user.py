#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""add password column to user

Revision ID: 561833c1c74b
Revises: 40e67319e3a9
Create Date: 2015-11-30 06:51:25.872557

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '561833c1c74b'
down_revision = '40e67319e3a9'
branch_labels = None
depends_on = None


def upgrade():   # noqa: D103
    op.add_column('user', sa.Column('password', sa.String(255)))


def downgrade():   # noqa: D103
    op.drop_column('user', 'password')
