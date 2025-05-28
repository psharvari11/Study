import express from 'express';
import {
  addBook,
  getBooks,
  updateBook,
  deleteBook,
  issueBook,
  returnBook
} from '../controllers/bookController.js';
import { protect, isAdmin } from '../middlewares/authMiddleware.js';

const router = express.Router();

router.route('/').get(getBooks).post(protect, isAdmin, addBook);
router.route('/:id')
  .put(protect, isAdmin, updateBook)
  .delete(protect, isAdmin, deleteBook);
router.post('/issue/:id', protect, issueBook);
router.post('/return/:id', protect, returnBook);

export default router;
