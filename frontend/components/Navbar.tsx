import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/" className="text-xl font-bold">
          E-Shop
        </Link>
        <div className="space-x-4">
          <Link href="/" className="hover:text-gray-300">
            Home
          </Link>
          <Link href="#" className="hover:text-gray-300">
            Products
          </Link>
          <Link href="#" className="hover:text-gray-300">
            Cart
          </Link>
        </div>
      </div>
    </nav>
  );
}
