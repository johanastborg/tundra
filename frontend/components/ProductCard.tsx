interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  image: string;
}

interface ProductCardProps {
  product: Product;
}

export default function ProductCard({ product }: ProductCardProps) {
  return (
    <div className="border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow">
      <div className="h-48 bg-gray-200 w-full object-cover flex items-center justify-center text-gray-500">
        {/* Placeholder for image */}
        <span>{product.name} Image</span>
      </div>
      <div className="p-4">
        <h3 className="font-semibold text-lg mb-2">{product.name}</h3>
        <p className="text-gray-600 text-sm mb-2">{product.description}</p>
        <div className="flex justify-between items-center mt-4">
          <span className="font-bold text-xl">${product.price.toFixed(2)}</span>
          <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
}
