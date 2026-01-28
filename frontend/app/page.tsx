import Navbar from "@/components/Navbar";
import ProductCard from "@/components/ProductCard";
import Footer from "@/components/Footer";

const DUMMY_PRODUCTS = [
  {
    id: 1,
    name: "Wireless Headphones",
    price: 99.99,
    description: "High-quality wireless headphones with noise cancellation.",
    image: "/placeholder.jpg",
  },
  {
    id: 2,
    name: "Smart Watch",
    price: 199.99,
    description: "Stay connected with this feature-packed smart watch.",
    image: "/placeholder.jpg",
  },
  {
    id: 3,
    name: "Laptop Backpack",
    price: 49.99,
    description: "Durable backpack with a padded laptop compartment.",
    image: "/placeholder.jpg",
  },
  {
    id: 4,
    name: "Mechanical Keyboard",
    price: 129.50,
    description: "Tactile mechanical keyboard for productivity and gaming.",
    image: "/placeholder.jpg",
  },
];

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8 text-center">Featured Products</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {DUMMY_PRODUCTS.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </main>
      <Footer />
    </div>
  );
}
