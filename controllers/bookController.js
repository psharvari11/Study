import Book from '../models/Book.js';

export const addBook = async (req, res) => {
  const { title, author, genre, year, totalCopies } = req.body;
  const newBook = new Book({ title, author, genre, year, totalCopies, availableCopies: totalCopies });
  await newBook.save();
  res.status(201).json(newBook);
};

export const getBooks = async (req, res) => {
  const books = await Book.find();
  res.json(books);
};

export const updateBook = async (req, res) => {
  const updatedBook = await Book.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(updatedBook);
};

export const deleteBook = async (req, res) => {
  await Book.findByIdAndDelete(req.params.id);
  res.json({ message: 'Book deleted' });
};

export const issueBook = async (req, res) => {
  const book = await Book.findById(req.params.id);
  if (!book || book.availableCopies < 1) return res.status(400).json({ message: 'Book not available' });

  book.availableCopies -= 1;
  await book.save();

  req.user.issuedBooks.push({
    bookId: book._id,
    issueDate: new Date(),
    returnDate: null
  });
  await req.user.save();

  res.json({ message: 'Book issued' });
};

export const returnBook = async (req, res) => {
  const book = await Book.findById(req.params.id);
  if (!book) return res.status(400).json({ message: 'Book not found' });

  book.availableCopies += 1;
  await book.save();

  const issueRecord = req.user.issuedBooks.find(
    (entry) => entry.bookId.toString() === book._id.toString() && !entry.returnDate
  );
  if (issueRecord) issueRecord.returnDate = new Date();

  await req.user.save();
  res.json({ message: 'Book returned' });
};
