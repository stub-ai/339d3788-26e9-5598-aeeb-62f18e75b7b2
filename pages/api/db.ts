import { NextApiRequest, NextApiResponse } from 'next'
import { Pool } from 'pg'

const pool = new Pool({
  user: 'dbuser',
  host: 'database.server.com',
  database: 'mydb',
  password: 'secretpassword',
  port: 5432,
})

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const client = await pool.connect()
  try {
    const { rows } = await client.query('SELECT * FROM my_table')
    res.status(200).json(rows)
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err })
  } finally {
    client.release()
  }
}