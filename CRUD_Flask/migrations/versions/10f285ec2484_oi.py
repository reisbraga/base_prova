"""oi

Revision ID: 10f285ec2484
Revises: 
Create Date: 2024-09-19 13:39:08.884556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f285ec2484'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Departamentos',
    sa.Column('id_departamento', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('responsavel', sa.String(length=100), nullable=True),
    sa.Column('numero_funcionarios', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_departamento')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Departamentos')
    # ### end Alembic commands ###
